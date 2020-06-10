#include "lists.h"
/**
 * check_cycle - checks if the linked list has a cycle.
 * @list: pointer to head of list.
 * Return: 1 if has cycle, otherwise 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *list1, *list2;

	if (list == NULL || list->next == NULL)
		return (0);

	list1 = list2 = list;

	while (list1 && list2 && list2->next)
	{
		list1 = list1->next;
		list2 = list2->next->next;

		if (list2 == list1)
			return (1);
	}

	return (0);
}