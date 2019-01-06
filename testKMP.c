int printf(const char *format,...);
int strlen(const char * s);

char s[] = "abcdefgabdef";
char t[] = "ab";

int next[1000];

void computeNext()
{
    int length_t = strlen(t);
    int index_t = 0;
    next[index_t] = 0;
    for(int index_moving = 1; index_moving < length_t + 1; ++index_moving)
    {
        while(index_moving < length_t && index_t < length_t && t[index_moving] == t[index_t])
        {
            ++index_t;
            ++index_moving;
            next[index_moving] = index_t;
        }
        if(index_moving == length_t)
        {
            next[index_moving] = index_t;
            break;
        }
        if(t[index_moving] != t[index_t])
        {
            while(index_t != 0 && t[index_moving] != t[index_t])
            {
                index_t = next[index_t];
            }
            next[index_moving] = index_t;
            continue;
        }
    }
}

int main()
{
    computeNext();
    int length_s = strlen(s);
    int length_t = strlen(t);
    if(length_t == 0)
    {
        printf("empty template string!\n");
        return 0;
    }
    int index_t = 0;
    for(int index_s = 0; index_s < length_s; )
    {
        while(index_s < length_s && index_t < length_t && s[index_s] == t[index_t])
        {
            ++index_t;
            ++index_s;
        }
        if(index_t == length_t)
        {
            printf("%d\n", index_s - length_t);
            index_t = next[index_t];
            continue;
        }
        if(index_s == length_s)
        {
            break;
        }
        while(index_t != 0 && s[index_s] != t[index_t])
        {
            index_t = next[index_t];
        }
        ++index_s;
    }
}