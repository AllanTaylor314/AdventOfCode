open Printf

exception InputError of string
exception NotInvertible

let process_line line =
  match String.split_on_char ':' line with
  | [ a; b ] ->
      ( int_of_string a,
        String.split_on_char ' ' b
        |> List.filter (fun s -> s <> "")
        |> List.map int_of_string )
  | _ -> raise (InputError (line ^ " is not a valid input line"))

let rec read_all () =
  match try read_line () with _ -> "" with
  | "" -> []
  | a -> process_line a :: read_all ()

let values = read_all ()
let any = List.fold_left ( || ) false
let unmul c b = if c mod b = 0 then c / b else raise NotInvertible
let unadd c b = if c >= b then c - b else raise NotInvertible
let rec minpow10 goal = if goal > 0 then 10 * minpow10 (goal / 10) else 1

let uncat c b =
  if c mod minpow10 b = b then c / minpow10 b else raise NotInvertible

let rec test unops goal rev_list =
  match rev_list with
  | [ a ] -> a = goal
  | a :: rest ->
      any
        (List.map
           (fun unop -> try test unops (unop goal a) rest with _ -> false)
           unops)
  | [] -> false

let is_reachable unops target list = test unops target (List.rev list)

let solve unops =
  List.map
    (fun p -> if is_reachable unops (fst p) (snd p) then fst p else 0)
    values
  |> List.fold_left ( + ) 0

let part1 = solve [ unadd; unmul ]
let part2 = solve [ unadd; unmul; uncat ]
let () = printf "Part 1: %d\nPart 2: %d\n" part1 part2
