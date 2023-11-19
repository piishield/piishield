import json
import os
import glob
import recognize
import time
from presidio_analyzer import AnalyzerEngine

analyzer = AnalyzerEngine()


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
                time.sleep(5)
                break
        time.sleep(5)
    print(f"There were {success} out of {len(evals)} total evals")
    return success

def perform_presidio_eval(location="../prompts/tests/presidio"):
    evals = load_evals(location)
    success = 0
    for eval in evals:
        if 'input' not in eval:
            continue
        print(eval)
        output = analyzer.analyze(text=eval["input"],
                           entities=["NRP", "CREDIT_CARD", "LOCATION", "PHONE_NUMBER", "PERSON"],
                           language='en')
        entity = output[0].entity_type
        print(entity)
        if entity == eval['output']:
            success += 1

    print(f"There were {success} successes out of {len(evals)} total evals")
    return success


def perform_openai_presidio_eval(location="../prompts/tests/presidio"):
    evals = load_evals(location)
    success = 0
    for eval in evals:
        if 'input' not in eval:
            continue
        print(eval)
        outputs = recognize.analyze_text(eval['input'], "../prompts/presidio")
        eval_output = eval['output']
        for output in outputs:
            output_json = json.loads(output)
            print(output_json)
            if eval_output in output_json:
                success += 1
                print("--Eval success")
                time.sleep(1)
                break
        time.sleep(1)
    print(f"There were {success} out of {len(evals)} total evals")
    return success


if __name__ == "__main__":
    perform_presidio_eval()
    perform_openai_presidio_eval()