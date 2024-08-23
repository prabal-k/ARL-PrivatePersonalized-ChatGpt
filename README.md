# Personalized Financial Chatgpt

This project demonstrates the fine-tuning of a LLaMA-2 7B model on custom finance data, aimed at enabling the model to effectively access and interpret individual financial information. Directly fine-tuning all 7 billion parameters in LLaMA-2 is resource-intensive, so Parameter-Efficient Fine-Tuning (PEFT) techniques, particularly Low-Rank Adaptation (LoRA), were employed. LoRA reduces the number of trainable parameters by injecting smaller, trainable matrices into the model layers, thus preserving performance while optimizing resources. The fine-tuning process was configured with:

Learning Rate: 2e-4 ,
Epochs: 6 ,
Batch Size: 2 ,
Rank: 64 ,
Scaling Factor (LoRA Alpha): 16 ,
Optimizer: paged_adamw_32bit ,
Weight Decay: 0.001


Training and Validation loss


![Training and validation loss over steps](https://github.com/user-attachments/assets/f09af8cf-891e-4ea6-b927-ecf9717dcc38)

Here you can see the full Project Implementation.

![Plant text-1](https://github.com/user-attachments/assets/13f6fb94-61b0-47fb-ae27-073d5c54ce30)


# Snapshot 


![Result-1](https://github.com/user-attachments/assets/5b490319-a21d-45bc-8542-b4dc01d381da)


![Result-2](https://github.com/user-attachments/assets/6d7b13f3-d9df-4aaf-be0b-cfcf7e9b950c)
