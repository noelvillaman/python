#include <stdio.h>
#include <math.h>

int values(int val);

int main()
{
  values(10);
  return 0;
}

int values(int val)
{
  int i, k, m, pc, j, p, myarray[val], mycomp[val], mypri[val];
  for(i = 0; i <val; i++)
    {
      myarray[i] = i + 1;
      //printf("%4d", myarray[i]);
    } 
  //printf("\n");
  k = 1;
  i = 0;
  p = 0;
  while(k <= sqrt(val))
    {
      if(myarray[i] > k){
	for(j = 0; j < val; j++){
	  m = myarray[i];
	  pc = myarray[j] * m;
	  for(p = 0; p < val; p++)
	    {
	      if(pc == myarray[p]) 
		mycomp[p] = pc;
	    }
	  mypri[j] = m;
	}
      k = m;
      i++;
      }
    }
  //now I need to merge the two arrays into one
  //int thetwo[val];
  //for (i = 0; i < val; i++)
  return mypri;

}
