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
        listint_t *node, *tmp;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		return (NULL);
	}
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
	}
	else
	{
		tmp = *head;
		if(tmp->n > node->n)
		{
			node->next = tmp;
			tmp = node;
			return (node);
		}
		while (tmp)
		{
			if (tmp->next == NULL || tmp->next->n > node->n)
                        {
				node->next = tmp->next;
				tmp->next = node;
				break;
			}
			tmp = tmp->next;
		}
	}
	return (node);
}
