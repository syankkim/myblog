---
title: CODING TEST with Java
tags: []
categories: []
thumbnail: ''
permalink: ''
date: 2020-04-22 16:03:14
---

<!-- excerpt -->
<!-- toc -->

```java
public static void main(String args[]){
        int[] nums = {2,1,1,2,5};
        int single = 0;
        List<Integer> list = Arrays.stream(nums).boxed().collect(Collectors.toList());

        for(int i=0; i<list.size(); i++){
            boolean isSingle = true;
            System.out.println("i : "+list.get(i));
            for(int j=i+1; j<list.size(); j++){

                System.out.println("i : "+i+"-"+list.get(i)+", j: "+j+"-"+list.get(j));
                if(list.get(i)==list.get(j)){
                    isSingle = false;
                    list.remove(list.get(i));
                    list.remove(list.get(j-1));
                    i--;
                    break;
                }
                System.out.println("list : " + list.toString());
            }
            System.out.println("isSingle : "+isSingle);
            if(isSingle){
                single = list.get(i);
                break;
            }
        }
        System.out.println("single : "+single);
    }
```