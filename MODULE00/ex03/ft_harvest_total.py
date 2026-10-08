# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: malavaud <malavaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/08 13:59:36 by malavaud          #+#    #+#              #
#    Updated: 2026/10/08 14:06:19 by malavaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day_one = int(input("Day 1 harvest: "))
	day_two = int(input("Day 2 harvest: "))
	day_three = int(input("Day 3 harvest: "))
	total = day_one + day_two + day_three
	print("Total harvest: ", total)