# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: malavaud <malavaud@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/08 15:04:35 by malavaud          #+#    #+#              #
#    Updated: 2026/10/09 09:22:14 by malavaud         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "packets":
		print(seed_type.capitalize(), "seeds:", quantity, "packets available")
	elif unit == "grams":
		print(seed_type.capitalize(), "seeds:", quantity, "grams total")
	elif unit == "area":
		print(seed_type.capitalize(), "seeds: covers", quantity, "sqaure meters")
	else:
		print("Unknown unit type")
