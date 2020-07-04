import torch
import torch.nn as nn
import torch.nn.functional as F

from transformer import BertPreTrainedModel, BertModel

class BertForClassificationWithLSTM(BertPreTrainedModel):
    """
    BERT model for classification with LSTM.
    This module is composed of the BERT model with a 
    LSTM layer on top of the pooled output.
    """
    
    def __init__(self, config, num_labels=2):
        super(BertForClassificationWithLSTM, self).__init__()
        self.num_labels = config.num_labels
        self.bert = BertModel(config)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.lstm = nn.LSTM(config.hidden_size, config.hidden_size, num_layer=1) # 수정 요망
        self.classificer = nnl.Linear(config.hidden_size, config.num_labels)
        self.apply(self.init_bert_weights)
        
    def forward(self, input_ids=None, attention_mask=None, token_type_ids=None,
                position_ids=None, head_mask=None, inputs_embeds=None, labels=None, output_attentions=None):
        
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
        )
        
        pooled_output = outputs[1]
        print (pooled_output.shape)
        
        pooled_output = self.dropout(pooled_output)
        logits = self.lstm(pooled_output)
        
        if labels is not None:
            loss_fct = nn.CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
        
        outputs = (loss,) + outputs
        
        return outputs
        

        
        
        
        
        