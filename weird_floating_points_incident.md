Computers store numbers in binary (base-2), not in our normal decimal (base-10) system and they can’t represent some decimal numbers exactly when using binary floating-point.

- In decimal, `0.1` is exact (1/10).
- In binary, `1/10` becomes an infinite repeating fraction:

  ```
  0.0001100110011001100110011001100110011...
  ```

  It goes on forever, just like 1/3 = 0.3333… repeats forever in decimal.

Because a computer has limited memory, it must cut off this repeating binary pattern after a certain number of bits (usually 52 bits for a 64-bit float).
So the stored value is close to, but not exactly, 0.1 or 0.2.
