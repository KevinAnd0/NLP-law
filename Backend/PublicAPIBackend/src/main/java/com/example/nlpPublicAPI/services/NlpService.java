package com.example.nlpPublicAPI.services;

import com.example.nlpPublicAPI.entities.Keywords;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;

@Service
public class NlpService {

    RestTemplate restTemplate = new RestTemplate();
    String url = "http://localhost:1000/";

    public String getKeywords() {
        String result = restTemplate.getForObject(url+"keywords", String.class);
        return result;
    }

    public String getTexts() {
        String result = restTemplate.getForObject(url+"texts", String.class);
        return result;
    }

    public String searchTextByWord() {
        String result = restTemplate.getForObject(url+"search/word", String.class);
        return result;
    }


}
