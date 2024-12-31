open Printf

let rec read_lines () =
  match try read_line () with _ -> "" with
  | "" -> []
  | a -> a :: read_lines ()

let pad c =
  match c with
  | 'A' -> (0, 2)
  | '^' -> (0, 1)
  | '<' -> (1, 0)
  | 'v' -> (1, 1)
  | '>' -> (1, 2)
  | '0' -> (0, 1)
  | '1' -> (-1, 0)
  | '2' -> (-1, 1)
  | '3' -> (-1, 2)
  | '4' -> (-2, 0)
  | '5' -> (-2, 1)
  | '6' -> (-2, 2)
  | '7' -> (-3, 0)
  | '8' -> (-3, 1)
  | '9' -> (-3, 2)
  | _ -> invalid_arg "Not part of the pad"

let rec string_repeat count string =
  if count > 0 then string ^ string_repeat (count - 1) string else ""

let step src dst =
  let src_loc = pad src in
  let dst_loc = pad dst in
  let si = fst src_loc in
  let sj = snd src_loc in
  let di = fst dst_loc in
  let dj = snd dst_loc in
  if (di, sj) = (0, 0) || (si, dj) = (0, 0) then
    string_repeat (dj - sj) ">"
    ^ string_repeat (si - di) "^"
    ^ string_repeat (di - si) "v"
    ^ string_repeat (sj - dj) "<"
    ^ "A"
  else
    string_repeat (sj - dj) "<"
    ^ string_repeat (si - di) "^"
    ^ string_repeat (di - si) "v"
    ^ string_repeat (dj - sj) ">"
    ^ "A"

let rec steps string =
  if String.length string > 1 then
    step (String.get string 0) (String.get string 1)
    ^ steps (String.sub string 1 (String.length string - 1))
  else ""

let codes = read_lines ()
let num_codes = List.map (fun x -> steps ("A" ^ x)) codes
let dir_codes = List.map (fun x -> steps ("A" ^ x)) num_codes
let dir_codes = List.map (fun x -> steps ("A" ^ x)) dir_codes
let lengths = List.map String.length dir_codes

let numeric_parts =
  List.map (fun x -> int_of_string (String.sub x 0 (String.length x - 1))) codes

let part1 =
  List.combine numeric_parts lengths
  |> List.map (fun p -> fst p * snd p)
  |> List.fold_left ( + ) 0

let rec deduplicate = function
  | a :: b :: rest ->
      if fst a = fst b then deduplicate ((fst a, snd a + snd b) :: rest)
      else a :: deduplicate (b :: rest)
  | last -> last

let rec count_pairs string =
  if String.length string > 1 then
    ((String.get string 0, String.get string 1), 1)
    :: count_pairs (String.sub string 1 (String.length string - 1))
  else []

let rec apply = function
  | [] -> []
  | p :: rest ->
      List.concat
        [
          count_pairs ("A" ^ step (fst (fst p)) (snd (fst p)))
          |> List.map (fun q -> (fst q, snd q * snd p));
          apply rest;
        ]

let rec repeat n func vals =
  if n > 0 then repeat (n - 1) func (func vals) else vals

let counts =
  List.map
    (fun x ->
      repeat 25
        (fun y -> apply y |> List.sort compare |> deduplicate)
        (deduplicate (List.sort compare (count_pairs ("A" ^ x)))))
    num_codes

let lengths = List.map (List.fold_left (fun a b -> a + snd b) 0) counts

let part2 =
  List.combine numeric_parts lengths
  |> List.map (fun p -> fst p * snd p)
  |> List.fold_left ( + ) 0

let () = printf "Part 1: %d\nPart 2: %d\n" part1 part2
