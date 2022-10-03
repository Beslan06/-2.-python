#чтобы не записывать много раз и длинный код в одном файле, можно подтянуть с другого файла hello.py
import hello
print(hello.f(1))

# или проще h вместо hello
import hello as h
print(h.f(1))