int strlen(const char* s);
int printf(const char *format,...);

int stackData[5000 * 2];
int stackNo = 0;
int initStack() {
    if (stackNo >= 2) {
        return 666;
    }
    if (stackNo < 0) {
        return 666;
    }
    int ans = stackNo;
    stackNo = stackNo + 1;
    stackData[5000 * stackNo] = 0;
    return ans;
}
void push(int stack, int tar) {
    if (stack >= 2) {
        return;
    }
    if (stack < 0) {
        return;
    }
    int length = stackData[stack * 5000];
    if (length < 0) {
        return;
    }
    if (length >= 4999) {
        return;
    }
    stackData[stack * 5000 + length + 1] = tar;
    stackData[stack * 5000] = length + 1;
}
int pop(int stack) {
    if (stack >= 2) {
        return 0;
    }
    if (stack < 0) {
        return 0;
    }
    int length = stackData[stack * 5000];
    if (length <= 0) {
        return 0;
    }
    stackData[stack * 5000] = length - 1;
    return stackData[stack * 5000 + length];
}
int stackEmpty(int stack) {
    if (stack >= 2) {
        return 1;
    }
    if (stack < 0) {
        return 1;
    }
    int length = stackData[stack * 5000];
    if (length == 0) {
        return 1;
    }
    return 0;
}
int getTop(int stack) {
    if (stack >= 2) {
        return 0;
    }
    if (stack < 0) {
        return 0;
    }
    int length = stackData[stack * 5000];
    if (length <= 0) {
        return 0;
    }
    return stackData[stack * 5000 + length];
}

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
    int num = initStack();
    int opt = initStack();
    int i = 0;
    int tmp = 0;
    int j;
    int strlen_t = strlen(str);

    while (stackEmpty(opt) != 1 || i < strlen_t)
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
            if (stackEmpty(opt) != 1 && str[i] == '\0') {
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