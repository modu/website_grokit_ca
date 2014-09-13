
# C++ Interview Question: Quicksort Mergesort

## Question and Notes

    Build the quicksort and mergesort algorithms.
    Discuss the space and time complexity.
    Discuss the impact if quicksort is implemented in-place or not.
    
    Mergesort
    - Know the average, best and worst cases
    - How to do the merge with a O(n) complexity
    --> have to consider that the sub-lists are sorted, so
        there is no need for an 'all-to-all' elements compare
        that would cost O(n^2).
    
    Quicksort
    - Remember to handle the case: guarantee converge, guarantee sort
    - Be careful that the pivot is not inserted in a group (or else
      it is possible that an iteration does not progress)
    - Recursion completion condition: - always progressing?
    
    TODO
    - Quicksort in place

## Code

    
    #include <iostream>
    #include <vector>
    #include <list>
    #include <cassert>
    
    using namespace std;
    
    template<class T_>
    bool isSorted(const T_* array, int size)
    {
      if(size <= 1)
        return true;
      T_ prev = array[0];
      for(int i = 1; i < size; ++i)
      {
        if(prev > array[i])
          return false;
        prev = array[i];
      }
      return true;
    }
    
    template<class T_>
    void print(const T_* array, int size)
    {
      cout<<"print(T_* array, int size)"<<endl;
      for(int i = 0; i < size; ++i)
      {
        cout<<array[i]<<endl;
      }
    }
    
    //! Assumes target has the proper size
    template<class T_>
    void join(const vector<T_>& left, const vector<T_>& right, int pivot, T_* target)
    {
      int target_pos = 0;
      for(size_t i = 0; i < left.size(); ++i)
      {
        target[target_pos] = left[i];
        ++target_pos;
      }
    
      target[target_pos] = pivot;
      target_pos++;
    
      for(size_t i = 0; i < right.size(); ++i)
      {
        target[target_pos] = right[i];
        ++target_pos;
      }
    }
    
    
    template<class T_>
    class Sorter
    {
    public:
      virtual void sort(T_* array, int size) const = 0;
    };
    
    Problems:
    - Memory allocation for every recursive call
    - List would be better than vector (push_back is O(1) instead of worst case O(n)),
      but kept vector to have the same interface in both implementations.
    template<class T_>
    class QuickSorter_Slow : public Sorter<T_>
    {
    public:
      virtual void sort(T_* array, int size) const
      {
        if(size <=1)
          return;
        if(size == 2 && array[0] <= array[1])
          return;
    
        const int pivot_pos = size/2;
        T_ pivot = array[pivot_pos];
    
        vector<T_> less;
        vector<T_> more;
        for(int i = 0; i < size; ++i)
        {
          if(i == pivot_pos)
            continue;
    
          if( array[i] < pivot )
            less.push_back( array[i] );
          else
            more.push_back( array[i] );
        }
        if(less.size() != 0)
          sort( &less[0], less.size() );
        if(more.size() != 0)
          sort( &more[0], more.size() );
    
        join(less, more, pivot, array);
      }
    };
    
    
    //Another quicksort, with the join operation not in a separate function
    void quicksort(vector<int>& array)
    {
      if(array.size() <= 1)
        return;
    
      vector<int> l;
      l.reserve( array.size() / 2 );
      vector<int> r;
      r.reserve( array.size() / 2 );
      
      int pivot = array[ array.size() / 2 ];
      for(size_t i = 0; i < array.size(); ++i)
      {
        //Super important how we treat pivot
        if( i == array.size() / 2 )
          continue;
    
        if(array[i] <= pivot)
          l.push_back( array[i] );
        else
          r.push_back( array[i] );
      }
    
      quicksort(l);
      quicksort(r);
    
      size_t i = 0;
      for(; i < l.size(); ++i)
      {
        array[i] = l[i];
      }
      array[i] = pivot;
      ++i;
      for(size_t j = 0; j < r.size(); ++j, ++i)
      {
        array[i] = r[j];
      }
    }
    
    //! 'Inplace' version
    template<class T_>
    class QuickSorter_Fast : public Sorter<T_>
    {
    public:
      virtual void sort(T_* array, int size) const
      {
      }
    };
    
    void mergesort(vector<int>& array)
    {
      if(array.size() <= 1)
        return;
    
      vector<int> l;
      l.resize( array.size()/2 + array.size()%2 );
      vector<int> r;
      r.resize( array.size()/2 );
    
      size_t l_i = 0;
      size_t r_i = 0;
      for(size_t i = 0; i < array.size(); ++i)
      {
        if( i < (array.size()/2 + array.size()%2) )
        {
          l[l_i] = array[i];
          ++l_i;
        }
        else
        {
          r[r_i] = array[i];
          ++r_i;
        }
      }
    
      mergesort(l);
      mergesort(r);
      
      l_i = 0;
      r_i = 0;
      for(size_t a_i = 0; a_i < array.size(); ++a_i)
      {
        if(l_i >= l.size())
        {
          array[a_i] = r[r_i];
          ++r_i;
          continue;
        }
        if(r_i >= r.size())
        {
          array[a_i] = l[l_i];
          ++l_i;
          continue;
        }
    
        if(l[l_i] <= r[r_i])
        {
          array[a_i] = l[l_i];
          ++l_i;
        }
        else
        {
          array[a_i] = r[r_i];
          ++r_i;
        }
      }
    }
    
    template<class T_>
    class MergeSort : public Sorter<T_>
    {
    public:
      virtual void sort(T_* array, int size) const
      {
        vector<T_> vArr;
        vArr.resize( size );
        memcpy( &vArr[0], array, size*sizeof(T_) );
        mergesort(vArr);
        memcpy( array, &vArr[0], size*sizeof(T_) );
      }
    };
    
    
    void test_sort(const Sorter<int>& sorter)
    {
      vector<int> arrShort;
      
      arrShort.push_back(20);
      arrShort.push_back(7);
      arrShort.push_back(12);
      arrShort.push_back(100);
      arrShort.push_back(1);
      arrShort.push_back(7);
      arrShort.push_back(123);
      arrShort.push_back(3);
      arrShort.push_back(7);
      arrShort.push_back(7);
      arrShort.push_back(2);
    
      assert( !isSorted( &arrShort[0], arrShort.size() ) );
      cout<<"Before sort:"<<endl;
      print( &arrShort[0], arrShort.size() );
      sorter.sort(&arrShort[0], arrShort.size());
      cout<<"After sort:"<<endl;
      print( &arrShort[0], arrShort.size() );
      assert( isSorted( &arrShort[0], arrShort.size() ) );
    
      const int arrLongSize = 10000;
      vector<int> arrLong;
      arrLong.resize(arrLongSize);
      for(int i = 0; i < arrLongSize; ++i)
      {
        arrLong[i] = rand();
      }
      sorter.sort(&arrLong[0], arrLong.size());
      assert( isSorted( &arrLong[0], arrLong.size() ) );
      //print( &arrLong[0], arrLong.size() );
    }
    
    int main()
    {
      cout<<"Begin"<<endl;
    
      test_sort( QuickSorter_Slow<int>() );
      //test_sort( QuickSorter_Fast<int>() );
      test_sort( MergeSort<int>() );
      
      cout<<"End"<<endl;
      return 0;
    }

## Code Output

    Begin
    Before sort:
    print(T_* array, int size)
    20
    7
    12
    100
    1
    7
    123
    3
    7
    7
    2
    After sort:
    print(T_* array, int size)
    1
    2
    3
    7
    7
    7
    7
    12
    20
    100
    123
    Before sort:
    print(T_* array, int size)
    20
    7
    12
    100
    1
    7
    123
    3
    7
    7
    2
    After sort:
    print(T_* array, int size)
    1
    2
    3
    7
    7
    7
    7
    12
    20
    100
    123
    End

