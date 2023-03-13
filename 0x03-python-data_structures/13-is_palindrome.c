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
	int i = 0, j;
	int *arr;
	listint_t *curr;

	curr = *head;

	arr = malloc(sizeof(int));

	if (*head != NULL)
	{
		while (curr->next != NULL)
		{
			arr[i] = curr->n;
			curr = curr->next;
			i++;
		}
		arr[i] = curr->n;
		for (j = 0; j <= i; j++, i--)
		{
			if (arr[j] != arr[i])
			{
				return (0);
			}
		}
	}
	free(arr);
	return (1);
}
