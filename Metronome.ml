open Printf;;

let metronome n =
  Printf.printf "%f\n" ((float_of_int n) /. 4.0)
;;

print_float