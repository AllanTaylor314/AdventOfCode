open Printf

let process_line line =
  String.split_on_char ' ' line
  |> List.map int_of_string

let rec read_all () =
  match try read_line () |> process_line with _ -> [] with
  | [] -> []
  | a -> a :: read_all ()

let values = read_all ()

let rec is_ascending_safe report =
  match report with
  | [] -> true
  | [ _ ] -> true
  | a :: b :: rest ->
      if a < b && a + 4 > b then is_ascending_safe (b :: rest) else false

let rec is_descending_safe report =
  match report with
  | [] -> true
  | [ _ ] -> true
  | a :: b :: rest ->
      if a > b && a - 4 < b then is_descending_safe (b :: rest) else false

let is_safe report =
  match report with
  | [] -> true
  | [ _ ] -> true
  | a :: b :: _ ->
      if a < b then is_ascending_safe report else is_descending_safe report

let part1 =
  List.map (fun x -> if is_safe x then 1 else 0) values
  |> List.fold_left ( + ) 0

let () = printf "Part 1: %d\n" part1

let rec is_kinda_safe_asc report =
  match report with
  | [] -> true
  | [ _ ] -> true
  | [ _; _ ] -> true
  | a :: b :: rest ->
      if b - a < 4 && b - a > 0 then is_kinda_safe_asc (b :: rest)
      else is_ascending_safe (a :: rest)

let rec is_kinda_safe_desc report =
  match report with
  | [] -> true
  | [ _ ] -> true
  | a :: b :: rest ->
      if a - b < 4 && a - b > 0 then is_kinda_safe_desc (b :: rest)
      else is_descending_safe (a :: rest)

let rec is_kinda_safe report =
  is_kinda_safe_asc report || is_kinda_safe_desc report
  || match report with [] -> true | _ :: rest -> is_safe rest

let part2 =
  List.map (fun x -> if is_kinda_safe x then 1 else 0) values
  |> List.fold_left ( + ) 0

let () = printf "Part 2: %d\n" part2
