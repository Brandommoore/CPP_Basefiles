/* **************************************************************************** */
/*                                                                              */
/*                                                         :::      ::::::::    */
/*    basefiles_gen.py                                   :+:      :+:    :+:    */
/*                                                     +:+ +:+         +:+      */
/*    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         */
/*                                                 +#+#+#+#+#+   +#+            */
/*    Created: 2022/10/18 18:56:07 by marvin            #+#    #+#              */
/*    Updated: 2022/10/18 18:56:07 by marvin           ###   ########.fr        */
/*                                                                              */
/* **************************************************************************** */

#ifndef __ZOMBIE_H__
# define __ZOMBIE_H__

#include <iostream>
#include <string>

class Zombie
{
	private:
		std::string	_name;

	public:
		Zombie( void );
		Zombie( std::string name );
		~Zombie();

		void		announce( void );
};

Zombie		*newZombie( std::string name );
void		randomChump ( std::string name );

#endif
