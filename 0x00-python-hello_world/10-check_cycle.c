#include "lists.h"

/**
  * check_cycle - Check for cycle in a singly linked list
  *
  * @list: The singly linked list
  *
  * Return: 1 if it is a cycle and 0 otherwise
  */

int check_cycle(listint_t *list)
{
	int iscycle = 0;

	listint_t *current = list;

	if (current == NULL || current->next == NULL)

		return (0);

	while (current->next)
	{
		if ((current->next - list) == 0)
		{
			iscycle = 1;

			break;
		}

		current = current->next;
	}

	return (iscycle);
}
