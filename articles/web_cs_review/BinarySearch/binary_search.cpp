#include <iostream>
#include <cassert>

using namespace std;

//! Assume array is sorted
int binarySearch_recursive(int* array, int lower, int higher, int target)
{
  int pos = (higher - lower)/2 + lower;

  if(array[pos] == target)
    return pos;
  else if(lower == higher)
    return -1;
  else if (array[pos] > target)
    return binarySearch_recursive(array, lower, pos, target);
  else
    return binarySearch_recursive(array, pos + 1, higher, target);

  return -1;
}

//! Assume array is sorted
int binarySearch_array(int* array, int lower, int higher, int target)
{
  for(int pos = (higher - lower)/2 + lower; lower != higher; pos = (higher - lower)/2 + lower)
  {
    if(array[pos] == target)
      return pos;

    if( array[pos] > target )
    {
      higher = pos;
    }
    else
    {
      lower = pos + 1;
    }

    if(array[lower] == target)
      return lower;
  }

  return -1;
}

int main()
{
  cout<<"Begin"<<endl;

  int array[] = {-18, -2, 0, 1, 7, 12, 100, 105, 119, 150, 3000};
  
  assert( 0 == binarySearch_recursive(array, 0, 10, -18) );
  assert( 1 == binarySearch_recursive(array, 0, 10, -2) );
  assert( 2 == binarySearch_recursive(array, 0, 10, 0) );
  assert( 3 == binarySearch_recursive(array, 0, 10, 1) );
  assert( 4 == binarySearch_recursive(array, 0, 10, 7) );
  assert( 5 == binarySearch_recursive(array, 0, 10, 12) );
  assert( 6 == binarySearch_recursive(array, 0, 10, 100) );
  assert( 7 == binarySearch_recursive(array, 0, 10, 105) );
  assert( 8 == binarySearch_recursive(array, 0, 10, 119) );
  assert( 9 == binarySearch_recursive(array, 0, 10, 150) );
  assert( 10 == binarySearch_recursive(array, 0, 10, 3000) );
  assert( -1 == binarySearch_recursive(array, 0, 10, 13) );
  assert( -1 == binarySearch_recursive(array, 0, 10, 123123) );
  assert( -1 == binarySearch_recursive(array, 0, 10, -123) );
  assert( -1 == binarySearch_recursive(array, 0, 10, -3) );

  assert( 0 == binarySearch_array(array, 0, 10, -18) );
  assert( 1 == binarySearch_array(array, 0, 10, -2) );
  assert( 2 == binarySearch_array(array, 0, 10, 0) );
  assert( 3 == binarySearch_array(array, 0, 10, 1) );
  assert( 4 == binarySearch_array(array, 0, 10, 7) );
  assert( 5 == binarySearch_array(array, 0, 10, 12) );
  assert( 6 == binarySearch_array(array, 0, 10, 100) );
  assert( 7 == binarySearch_array(array, 0, 10, 105) );
  assert( 8 == binarySearch_array(array, 0, 10, 119) );
  assert( 9 == binarySearch_array(array, 0, 10, 150) );
  assert( 10 == binarySearch_array(array, 0, 10, 3000) );
  assert( -1 == binarySearch_array(array, 0, 10, 13) );
  assert( -1 == binarySearch_array(array, 0, 10, 123123) );
  assert( -1 == binarySearch_array(array, 0, 10, -123) );
  assert( -1 == binarySearch_array(array, 0, 10, -3) );

  cout<<"End"<<endl;
  return 0;
}
