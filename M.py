def machine():
    interp = 'def machine():\n\tinterp=%r\n\tprint(interp%%interp)'
    print(interp%interp, '\n', interp%interp)
