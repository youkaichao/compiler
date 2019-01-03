let s = "abcdefgabdef";
let t = "ab";
let next = new Array(1000);
function computeNext() 
{
  let length_t = t.length;
  let index_t = 0;
  next[index_t] = 0;
  for (let index_moving = 1; index_moving < length_t + 1; ++ index_moving)
  {
    while(index_moving < length_t && index_t < length_t && t[index_moving] === t[index_t])
    {
      ++ index_t;
      ++ index_moving;
      next[index_moving] = index_t;
    }
    if(index_moving === length_t)
    {
      next[index_moving] = index_t;
      break;
    }
    if(t[index_moving] !== t[index_t])
    {
      while(index_t !== 0 && t[index_moving] !== t[index_t])
      {
        index_t = next[index_t];
      }
      next[index_moving] = index_t;
      continue;
    }
  }
}
function main() 
{
  computeNext();
  let length_s = s.length;
  let length_t = t.length;
  if(length_t === 0)
  {
    console.log("empty template string!");
    return 0;
  }
  let index_t = 0;
  for (let index_s = 0; index_s < length_s; )
  {
    while(index_s < length_s && index_t < length_t && s[index_s] === t[index_t])
    {
      ++ index_t;
      ++ index_s;
    }
    if(index_t === length_t)
    {
      console.log("%d", index_s - length_t);
      index_t = next[index_t];
      continue;
    }
    if(index_s === length_s)
    {
      break;
    }
    while(index_t !== 0 && s[index_s] !== t[index_t])
    {
      index_t = next[index_t];
    }
    ++ index_s;
  }
}
main()
