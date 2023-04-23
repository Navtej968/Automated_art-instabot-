import random 
promptfile1 = open('prompt1.txt','r')
promptfile2 = open('prompt2.txt','r')

prompt_list1 = [line.split('\n') for line in promptfile1]
prompt_list2 = [line.split('\n') for line in promptfile2]
def get_prompt():
  prompt =''
  for i in range(2):
    prompt = prompt + prompt_list1[random.randrange(0,183)][0] +"," +prompt_list2[random.randrange(0,492)][0]+ ","
  return(prompt)

style_list =[
  'enhance' , 'anime' ,'photographic' ,'digita-art' , 'comic-book' , 'fantasy-art' , 'line-art' , 'analog-film' , 'neon-punk' , 'isometric' , 'low-poly' , 'origami' , 'modeling-compound' , 'cinematic' , '3d-model' , 'pixek-art' , 'tile-texture'
]

