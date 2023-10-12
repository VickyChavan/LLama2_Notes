!pip install autotrain-advanced 
!pip install huggingface_hub
!autotrain setup --update-torch 
from huggingface_hub import notebook_login
notebook_login() 
!autotrain llm --train --project_name 'llama2_Health' --model "meta-llama/Llama-2-7b-chat-hf" --data_path "/content/sample_data" --text_column 'ICD_and_Health' --use_peft --use_int4 --learning_rate 0.1 --train_batch_size 5 --num_train_epochs=2 --trainer "sft" --model_max_length 2048 --push_to_hub --repo_id "Abhiijit01/Conversational"
