#include <stdio.h>
#include <stdlib.h>
#define INT_MAX 1000000000000000000


struct AdjListNode
{
    int dest;
    unsigned long long int weight;
    struct AdjListNode* next;
};


struct AdjList
{
    struct AdjListNode *head;
};

struct Graph
{
    int V;
    struct AdjList* array;
};

struct AdjListNode* newAdjListNode(int dest, unsigned long long int weight)
{
    struct AdjListNode* newNode =
            (struct AdjListNode*) malloc(sizeof(struct AdjListNode));
    newNode->dest = dest;
    newNode->weight = weight;
    newNode->next = NULL;
    return newNode;
}

struct Graph* createGraph(int V)
{
    int i;
    struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
    graph->V = V;

    graph->array = (struct AdjList*) malloc(V * sizeof(struct AdjList));

    for (i = 0; i < V; ++i)
        graph->array[i].head = NULL;

    return graph;
}

void add(struct Graph* graph, int src, int dest, unsigned long long int weight)
{

    struct AdjListNode* newNode = newAdjListNode(dest, weight);
    newNode->next = graph->array[src].head;
    graph->array[src].head = newNode;

    newNode = newAdjListNode(src, weight);
    newNode->next = graph->array[dest].head;
    graph->array[dest].head = newNode;
}

struct MinHeapNode
{
    int  v;
    unsigned long long int dist;
};

struct MinHeap
{
    int size;
    int capacity;
    int *pos;
    struct MinHeapNode **array;
};

struct MinHeapNode* newMinHeapNode(int v, unsigned long long int dist)
{
    struct MinHeapNode* minHeapNode =
           (struct MinHeapNode*) malloc(sizeof(struct MinHeapNode));
    minHeapNode->v = v;
    minHeapNode->dist = dist;
    return minHeapNode;
}

struct MinHeap* createMinHeap(int capacity)
{
    struct MinHeap* minHeap =
         (struct MinHeap*) malloc(sizeof(struct MinHeap));
    minHeap->pos = (int *)malloc(capacity * sizeof(int));
    minHeap->size = 0;
    minHeap->capacity = capacity;
    minHeap->array =
         (struct MinHeapNode**) malloc(capacity * sizeof(struct MinHeapNode*));
    return minHeap;
}

void swapMinHeapNode(struct MinHeapNode** a, struct MinHeapNode** b)
{
    struct MinHeapNode* t = *a;
    *a = *b;
    *b = t;
}


void minHeapify(struct MinHeap* minHeap, int idx)
{
    int smallest, left, right;
    smallest = idx;
    left = 2 * idx + 1;
    right = 2 * idx + 2;

    if (left < minHeap->size &&
        minHeap->array[left]->dist < minHeap->array[smallest]->dist )
      smallest = left;

    if (right < minHeap->size &&
        minHeap->array[right]->dist < minHeap->array[smallest]->dist )
      smallest = right;

    if (smallest != idx)
    {

        MinHeapNode *smallestNode = minHeap->array[smallest];
        MinHeapNode *idxNode = minHeap->array[idx];


        minHeap->pos[smallestNode->v] = idx;
        minHeap->pos[idxNode->v] = smallest;

        swapMinHeapNode(&minHeap->array[smallest], &minHeap->array[idx]);

        minHeapify(minHeap, smallest);
    }
}

int isEmpty(struct MinHeap* minHeap)
{
    return minHeap->size == 0;
}

struct MinHeapNode* extractMin(struct MinHeap* minHeap)
{
    if (isEmpty(minHeap))
        return NULL;

    struct MinHeapNode* root = minHeap->array[0];

    struct MinHeapNode* lastNode = minHeap->array[minHeap->size - 1];
    minHeap->array[0] = lastNode;

    minHeap->pos[root->v] = minHeap->size-1;
    minHeap->pos[lastNode->v] = 0;

    --minHeap->size;
    minHeapify(minHeap, 0);

    return root;
}

void decreaseKey(struct MinHeap* minHeap, int v, unsigned long long int dist)
{

    int i = minHeap->pos[v];

    minHeap->array[i]->dist = dist;

    while (i && minHeap->array[i]->dist < minHeap->array[(i - 1) / 2]->dist)
    {
        minHeap->pos[minHeap->array[i]->v] = (i-1)/2;
        minHeap->pos[minHeap->array[(i-1)/2]->v] = i;
        swapMinHeapNode(&minHeap->array[i],  &minHeap->array[(i - 1) / 2]);

        // move to parent index
        i = (i - 1) / 2;
    }
}

bool isInMinHeap(struct MinHeap *minHeap, int v)
{
   if (minHeap->pos[v] < minHeap->size)
     return true;
   return false;
}

void printArr(unsigned long long int dist[], int n)
{
    for (int i = 0; i < n; ++i)
        printf("%llu ", dist[i]);
    printf("\n");
}

void shortest(struct Graph* graph, int src, int flag, int k, unsigned long long int x, int shutPro)
{
    int V = graph->V;
    unsigned long long int dist[V];

    struct MinHeap* minHeap = createMinHeap(V);

    for (int v = 0; v < V; ++v)
    {
        dist[v] = INT_MAX;
        minHeap->array[v] = newMinHeapNode(v, dist[v]);
        minHeap->pos[v] = v;
    }

    minHeap->array[src] = newMinHeapNode(src, dist[src]);
    minHeap->pos[src]   = src;
    dist[src] = 0;
    decreaseKey(minHeap, src, dist[src]);

    minHeap->size = V;

    while (!isEmpty(minHeap))
    {

        struct MinHeapNode* minHeapNode = extractMin(minHeap);
        int u = minHeapNode->v;

        struct AdjListNode* pCrawl = graph->array[u].head;
        while (pCrawl != NULL)
        {
            int v = pCrawl->dest;

            if (isInMinHeap(minHeap, v) && dist[u] != INT_MAX &&
                                          pCrawl->weight + dist[u] < dist[v])
            {
                dist[v] = dist[u] + pCrawl->weight;

                decreaseKey(minHeap, v, dist[v]);
            }
            pCrawl = pCrawl->next;
        }
    }
    if(flag==1  && shutPro!=1){
        int v, edge;
        unsigned long long int min = INT_MAX;
        for(v=0;v<k;v++){
            if(min>dist[v]){
                min=dist[v];
                edge = v;
            }
        }
            for(int i=0;i<k;i++)
                add(graph, edge, i, x);
            shortest(graph, src, 1, k, x, 1);

    }else{
        printArr(dist, V);
    }
}

int main(){
    int t, n, s, i, j, k, d, flag=0;
    unsigned long long int x, y;
    scanf("%d", &t);
    while(t--){
        scanf("%d %d %llu %d %d", &n,&k,&y,&d,&s);

        struct Graph* graph = createGraph(n);

        s-=1;
        flag = 0;


        if(s<k){
            flag=0;
            while(d--){
                scanf("%d %d %llu", &i, &j, &x);

                add(graph, i-1, j-1, x);
            }
            for(i=0;i<k;i++){
                if(i!=s)
                    add(graph, i, s, y);
            }
        }
        else {
            if(k>500) {
                flag=1;
                while(d--){
                    scanf("%d %d %llu", &i, &j, &x);
                    add(graph, i-1, j-1, x);
                }
            }
            else {
                flag=0;
                for(i=0;i<k-1;i++){
                    for(j=i+1;j<k;j++){
                        add(graph, i, j, y);
                    }
                }
                while(d--){
                    scanf("%d %d %llu", &i, &j, &x);
                    add(graph, i-1, j-1, x);
                }
            }
        }
        shortest(graph, s, flag, k, y, 0);
    }
    return 0;
}
