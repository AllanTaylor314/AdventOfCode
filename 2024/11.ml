open Printf

let start_vals =
  read_line () |> String.split_on_char ' ' |> List.map int_of_string

let init_counts = List.map (fun x -> (x, 1)) start_vals
let rec minpow10 goal = if goal > 0 then 10 * minpow10 (goal / 10) else 1
let rec minpow100 goal = if goal > 0 then 100 * minpow100 (goal / 100) else 1
let rec semipow10 goal = if goal > 0 then 10 * semipow10 (goal / 100) else 1

let rec step counts =
  match counts with
  | [] -> []
  | p :: rest ->
      if fst p = 0 then (1, snd p) :: step rest
      else if minpow10 (fst p) = minpow100 (fst p) (*Even*) then
        (fst p / semipow10 (fst p), snd p)
        :: (fst p mod semipow10 (fst p), snd p)
        :: step rest
      else (fst p * 2024, snd p) :: step rest

let rec deduplicate counts =
  match counts with
  | [] -> []
  | [ _ ] -> counts
  | a :: b :: rest ->
      if fst a = fst b then deduplicate ((fst a, snd a + snd b) :: rest)
      else a :: deduplicate (b :: rest)

let rec steps reps counts =
  if reps > 0 then steps (reps - 1) (step counts |> List.sort compare |> deduplicate) else counts

let part1 = steps 25 init_counts |> List.map snd |> List.fold_left ( + ) 0
let part2 = steps 75 init_counts |> List.map snd |> List.fold_left ( + ) 0
let () = printf "Part 1: %d\nPart 2: %d\n" part1 part2
