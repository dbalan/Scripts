#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <sys/wait.h>
#include <string.h>
#include <unistd.h>

int *setup_val()
{
  key_t seg_key;

  seg_key = ftok("value", 1);

  if (0 > seg_key)
    {
      perror("ftok");
    }
  int *sharedval;
  int shmid = shmget(seg_key, sizeof(int),IPC_CREAT);

  if(0>shmid)
    {
      perror("E: SHMGET Failed");
    }

  sharedval = (int *) shmat(shmid, NULL,0);
  if(0 > sharedval)
    {
      perror("E: SHMAT Failed!");
    }
  *sharedval = 0;
  return sharedval;
}

char *read_line(char *prompt)
{
  char *input;
  if(prompt != NULL);
  {
    printf("%s",prompt);
  }
  size_t length=20*sizeof(char);

  getline(&input,&length,stdin);
  return input;
}

int main()
{
  char *expr;
  expr = read_line("Enter expression:");
  /*  child = fork();

  if(child == 0)
    {
      *sharedval += 2;
    }
  else
    {
      *sharedval += 2;
      int stat;
      while(wait(&stat) > 0);
      printf("value: %d\n", *sharedval);
    }
  */
  return 0;

}
