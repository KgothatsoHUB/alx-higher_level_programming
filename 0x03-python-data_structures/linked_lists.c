#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    size_t n = 0;

    while (h != NULL)
    {
        printf("%i\n", h->n);
        h = h->next;
        n++;
    }

    return n;
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in the new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new = malloc(sizeof(listint_t));
    if (new == NULL)
        return NULL;

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        listint_t *current = *head;
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return new;
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to the list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}

int main()
{
    // Example usage:
    listint_t *myList = NULL;

    add_nodeint_end(&myList, 10);
    add_nodeint_end(&myList, 20);
    add_nodeint_end(&myList, 30);

    printf("Number of nodes: %zu\n", print_listint(myList));

    free_listint(myList);

    return 0;
}
