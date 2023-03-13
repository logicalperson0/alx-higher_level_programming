#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - fun that cheacks if singly linked list
 * is palindrome or not
 *
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 for is palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (chking(head, *head));
}

/**
 * chking - fun to chk list
 * @first: ptr to a ptr to beginning of list
 * @end: ptr to end of list
 *
 * Return: 1 for success 0 otherwise
 */
int chking(listint_t **first, listint_t *end)
{
	if (end == NULL)
		return (1);

	if (chking(first, end->next) && (*first)->n == end->n)
	{
		*first = (*first)->next;
		return (1);
	}
	return (0);
}
