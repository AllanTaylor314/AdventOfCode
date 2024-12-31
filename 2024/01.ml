open Printf

let process_line line =
  List.map int_of_string
  @@ List.filter (fun s -> s <> "")
  @@ String.split_on_char ' ' line

let rec read_all =
 fun () ->
  match try read_line () |> process_line with _ -> [] with
  | [] -> []
  | a -> a :: read_all ()

let values = read_all ()

let left_list =
  List.sort compare
  @@ List.map (fun pair -> match pair with a :: _ -> a | _ -> 0) values

let right_list =
  List.sort compare
  @@ List.map (fun pair -> match pair with _ :: a :: _ -> a | _ -> 0) values

let rec part1 =
 fun left right ->
  match left with
  | top_left :: remaining_left -> (
      match right with
      | top_right :: remaining_right ->
          abs (top_left - top_right) + part1 remaining_left remaining_right
      | [] -> 0)
  | [] -> 0

let () = printf "Part 1: %d\n" (part1 left_list right_list)

let rec count_occurrence =
 fun needle haystack ->
  match haystack with
  | top :: remaining ->
      (if top = needle then 1 else 0) + count_occurrence needle remaining
  | [] -> 0

let rec part2 =
 fun left right ->
  match left with
  | top :: remaining ->
      (top * count_occurrence top right) + part2 remaining right
  | [] -> 0

let () = printf "Part 2: %d\n" (part2 left_list right_list)
