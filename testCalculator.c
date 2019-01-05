int strlen(const char* s);
int printf(const char *format,...);
int* initStack(int* len);
void push(int* stack, int tar);
int pop(int* stack);
int stackEmpty(int* stack);
int getTop(int* stack);

char str[] = "5+6*(3+2)-1";

int Priority(int s)
{
    if (s == '(')
    {
        return 3;
    }
    if (s == '*' || s == '/') {
        return 2;
    }
    if (s == '+' || s == '-') {
        return 1;
    }
    return 0;
}

int main()
{
    int* num = initStack();
    int* opt = initStack();
    int i = 0;
    int tmp = 0;
    int j;
    int strlen_t = strlen(str);

    while (stackEmpty(opt) != true || i < strlen_t)
    {
        if(str[i] >= '0' && str[i] <= '9')
        {
            tmp = tmp * 10 + str[i] - '0';
            i = i + 1;
            if(str[i] >= '0' && str[i] <= '9') {
                continue;
            }
            else {
                push(num, tmp);
                tmp = 0;
            }
        }
        else
        {
            if(stackEmpty(opt) || Priority(str[i]) > Priority(getTop(opt)))
            {
                push(opt, str[i]);
                i = i + 1;
                continue;
            }
            if (getTop(opt) == '(' && str[i] != ')') {
                push(opt, str[i]);
                i = i + 1;
                continue;
            }
            if(getTop(opt) == '(' && str[i] == ')')
            {
                pop(opt);
                i = i + 1;
                continue;
            }
            int ok = 0;
            if (stackEmpty(opt) != true && str[i] == '\0') {
                ok = 1;
            }
            if(str[i] == ')' && getTop(opt) != '(') {
                ok = 1;
            }
            if (Priority(str[i]) <= Priority(getTop(opt))) {
                ok = 1;
            }
            if (ok) {
                int opt_now = pop(opt);
                if (opt_now ==  '+') {
                    push(num, pop(num) + pop(num));
                }
                if (opt_now ==  '-') {
                    j = pop(num);
                    push(num, pop(num) - j);
                }
                if (opt_now ==  '*') {
                    push(num, pop(num) * pop(num));
                }
                if (opt_now ==  '/') {
                    j = pop(num);
                    push(num, pop(num) / j);
                }
            }
        }
    }

    printf("%d\n", pop(num));
    return 0;
}