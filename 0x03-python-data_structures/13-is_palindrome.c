#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - A function that checks if a list is a palindrome.
 * @head: A pointer to the pointer to the head of the linked list
 * Return: 0 if the list is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *hare = *head;
	listint_t *tortoise = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /*its a palindrome */
	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		temp = tortoise->next;
		tortoise->next = prev;
		prev = tortoise;
		tortoise = temp;
	}

	if (hare != NULL)
		tortoise = tortoise->next;

	while (prev != NULL && tortoise != NULL)
	{
		if (prev->n != tortoise->n)
			return (0);
		prev = prev->next;
		tortoise = tortoise->next;
	}

	return (1);
}

