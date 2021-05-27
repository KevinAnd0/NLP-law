package com.example.nlpPublicAPI.services;

import com.example.nlpPublicAPI.entities.Keywords;
import org.apache.tomcat.util.json.JSONParser;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;

@Service
public class NlpService {

    RestTemplate restTemplate = new RestTemplate();
    String url = "http://localhost:5000/";
    
}
