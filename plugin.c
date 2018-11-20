#include <stdlib.h>
#include <stdio.h>
int len(char* ar){
  int i=0;
  while(ar[i]!='\0'){
    i++;
  }
  return i;
}
int numOfWords(char* ar,int length){
  int size = 0;
  for(int i=0;i<length;i++){
    if(ar[i]=='\n'){
      size++;
    }
  }
  return size+1;
}
char** divide(char* ar,char sym){
  int length = len(ar);
  int size =numOfWords(ar,length);
  int insert =0;
  char** res = (char**) malloc((size)*sizeof(char*));
  char* tmp = (char*) malloc((length+1)*sizeof(char));
  for(int i=0;i<=length;i++){
    tmp[i] = ar[i];
    if(tmp[i]==sym) tmp[i] = '\0';
  }
  int x=0;
  for(int i=0;i<=length;i++){
    if(tmp[i]=='\0'){
      res[insert] = &tmp[x];
      x = i+1;
      insert++;
    }
  }
  return res;
}


void main(){
  FILE* file = fopen("plugins.binary","r");
  if(file!=NULL){
    char c;
    int index = 0;
    char str[8000];
    while((c=fgetc(file))!=EOF){
      str[index] = c;
      index++;
    }
    str[index] = '\0';
    char** com = divide(str,'\n');
    int num = numOfWords(str,len(str));
    for(int i=0;i<num;i++){
      system(com[i]);
    }
  }
}
