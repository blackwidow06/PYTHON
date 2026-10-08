# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: malavaud <malavaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/08 14:30:35 by malavaud          #+#    #+#              #
#    Updated: 2026/10/08 15:02:15 by malavaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_days(day, days):
	print("Day", day)
	if (day < days):
		ft_count_days(day + 1, days)

def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	ft_count_days(1, days)
	print("Harvest time!")