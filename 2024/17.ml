open Printf

exception InvalidOpcode
exception NoSolution

let registerA =
  List.nth (read_line () |> String.split_on_char ' ') 2 |> int_of_string

let _ = read_line ()
let _ = read_line ()
let _ = read_line ()

let program_list =
  List.nth (read_line () |> String.split_on_char ' ') 1
  |> String.split_on_char ',' |> List.map int_of_string

let program = Array.of_list program_list
let combo_lut a b c n = match n with 4 -> a | 5 -> b | 6 -> c | _ -> n

let rec exec prog ip a b c =
  try
    let opcode = prog.(ip) in
    let operand = prog.(ip + 1) in
    let combo = combo_lut a b c operand in
    match opcode with
    | 0 -> exec prog (ip + 2) (Int.shift_right a combo) b c
    | 1 -> exec prog (ip + 2) a (Int.logxor b operand) c
    | 2 -> exec prog (ip + 2) a (combo mod 8) c
    | 3 -> exec prog (if a <> 0 then operand else ip + 2) a b c
    | 4 -> exec prog (ip + 2) a (Int.logxor b c) c
    | 5 -> (combo mod 8) :: exec prog (ip + 2) a b c
    | 6 -> exec prog (ip + 2) a (Int.shift_right a combo) c
    | 7 -> exec prog (ip + 2) a b (Int.shift_right a combo)
    | _ -> raise InvalidOpcode
  with Invalid_argument _ -> []

let run_with a = exec program 0 a 0 0
let part1 = run_with registerA |> List.map string_of_int |> String.concat ","

let options lol =
  List.map
    (fun a -> List.map (fun b -> (a * 8) + b) [ 0; 1; 2; 3; 4; 5; 6; 7 ])
    lol
  |> List.flatten

let rec find_inputs_for_suffix suffix =
  List.filter
    (fun n -> suffix = run_with n)
    (match suffix with
    | [] -> raise (Invalid_argument "Empty suffix")
    | [ _ ] -> [ 0; 1; 2; 3; 4; 5; 6; 7 ]
    | _ :: rest -> options (find_inputs_for_suffix rest))

let part2 = List.nth (find_inputs_for_suffix program_list) 0
let () = printf "Part 1: %s\nPart 2: %d\n" part1 part2
