import json
import os
import glob
import recognize
import time


def load_evals(location):
    files = glob.glob(f"{location}/*.jsonl")
    eval_strs = []
    for file in files:
        with open(file, 'r') as f:
            lines = [line.rstrip() for line in f]
            eval_strs.append(lines)
    evals = []
    for eval_str in eval_strs:
        for eval_json in eval_str:
            evals.append(json.loads(eval_json))
    return evals

def perform_eval(location="../prompts/tests/recognize"):
    evals = load_evals(location)
    success = 0
    for eval in evals:
        if 'input' not in eval:
            continue
        print(eval)
        outputs = recognize.analyze_text(eval['input'])
        for i in range(len(outputs)):
            outputs[i] = outputs[i].lower()
        eval_json = json.loads(eval['output'].lower())
        eval_key = list(eval_json.keys())[0]
        for output in outputs:
            output_json = json.loads(output)
            if eval_key in output_json and eval_json[eval_key] == output_json[eval_key]:
                success += 1
                print("--Eval success")
                time.sleep(15)
                break
        time.sleep(15)
    print(f"There were {success} out of {len(evals)} total evals")
    return success




if __name__ == "__main__":
    perform_eval()