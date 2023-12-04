#include "lists.h"


/**
 * reverse_listint - reverse a linked ls
 * @head: pointer to the 1st node in the ls
 *
 * Return: pointer to the 1st node in the new ls
 */
void reverse_listint(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;


  while (current)
    {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
    }


  *head = prev;
}


/**
 * is_palindrome - check if linked ls ispalindrome
 * @head: dbl pointer to the linked ls
 *
 * Return: 1 if it is, 0 not
 */
int is_palindrome(listint_t **head)
{
  listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;


  if (*head == NULL || (*head)->next == NULL)
    return (1);


  while (1)
    {
      fast = fast->next->next;
      if (!fast)
        {
          dup = slow->next;
          break;
        }
      if (!fast->next)
        {
          dup = slow->next->next;
          break;
        }
      slow = slow->next;
    }


  reverse_listint(&dup);


  while (dup && temp)
    {
      if (temp->n == dup->n)
        {
          dup = dup->next;
          temp = temp->next;
        }
      else
        return (0);
    }


  if (!dup)
    return (1);


  return (0);
}
