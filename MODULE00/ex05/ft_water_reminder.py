# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: malavaud <malavaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/08 14:19:47 by malavaud          #+#    #+#              #
#    Updated: 2026/10/08 14:26:28 by malavaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	last_watering = int(input("Days since last watering: "))
	if (last_watering > 2):
		print("Water the plants!")
	else:
		print("Plants are fine")