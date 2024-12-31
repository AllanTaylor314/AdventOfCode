open Printf

exception InputError of string

let process_rule line =
  match String.split_on_char '|' line |> List.map int_of_string with
  | [ a; b ] -> (a, b)
  | _ -> raise (InputError (line ^ " is not a valid pair"))

let process_group line = String.split_on_char ',' line |> List.map int_of_string

let rec read_rules () =
  match read_line () with "" -> [] | a -> process_rule a :: read_rules ()

let rec read_groups () =
  match try read_line () |> process_group with _ -> [] with
  | [] -> []
  | a -> a :: read_groups ()

let rules = read_rules ()
let groups = read_groups ()

let rec contains list value =
  match list with
  | [] -> false
  | a :: rest -> if a = value then true else contains rest value

let sorted_groups =
  List.map
    (List.sort (fun a b ->
         if a = b then 0 else if contains rules (a, b) then -1 else 1))
    groups

let middle list = List.nth list (List.length list / 2)

let part1 =
  List.combine groups sorted_groups
  |> List.map (fun p -> if fst p = snd p then middle (fst p) else 0)
  |> List.fold_left ( + ) 0

let part2 = (List.map middle sorted_groups |> List.fold_left ( + ) 0) - part1
let () = printf "Part 1: %d\nPart 2: %d\n" part1 part2
