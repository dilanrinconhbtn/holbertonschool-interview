#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node, *tmp;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		free(node);
		return (NULL);
	}
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
		*head = node;
	else
	{
		tmp = *head;
		while (tmp->next == NULL)
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
