int strlen(const char* s);
int printf(const char *format,...);

char t[] = "ese";

int main()
{
    int length_t = strlen(t);
    int first = 0, last = length_t - 1;
    int is_palin = 1;
    while(first < last)
    {
        if(t[first] == t[last])
        {
            ++first;
            --last;
        }else{
            is_palin = 0;
            break;
        }
    }
    if(is_palin)
    {
        printf("wow, it is palindrome!\n");
    }else{
        printf("oops, it is not palindrome!\n");
    }
}