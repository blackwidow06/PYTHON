# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: malavaud <malavaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/08 14:07:09 by malavaud          #+#    #+#              #
#    Updated: 2026/10/08 14:16:45 by malavaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	plant_age = int(input("Enter plant age in days: "))
	if (plant_age > 60):
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")