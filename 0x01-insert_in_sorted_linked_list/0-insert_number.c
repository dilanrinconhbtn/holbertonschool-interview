#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Print elements of a linked list
 * @head: pointer to head
 * @number: new node
 * Return: new node position
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;


	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;
	if (*head == NULL)
	{
		*head = newnode;
		return (newnode);
	}
	if (newnode->n < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
		temp = *head;
		while (temp != NULL)
		{

			if (temp->next == NULL || temp->next->n > newnode->n)
			{
				newnode->next = temp->next;
				temp->next = newnode;
				break;
			}
			temp = temp->next;
		}
	}
	return (newnode);
}
