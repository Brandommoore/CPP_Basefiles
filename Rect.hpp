// Rect.hpp
//

#ifndef __RECT_H__
# define __RECT_H__

# include <iostream>
# include <stdlib.h>

class Rect
{

private:
	int	_width;
	int	_height;

public:
	Rect( int width, int height );
	void	perimeter();
	void	area();

};

#endif

