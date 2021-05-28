package com.example.nlpPublicAPI.controllers;

import com.example.nlpPublicAPI.entities.Keywords;
import com.example.nlpPublicAPI.services.NlpService;
import org.apache.tomcat.util.json.JSONParser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;

@RestController
public class NlpController {

    @Autowired
    NlpService nlpservice;

    @GetMapping("/")
    public String index(){
        System.out.println("Test");
        return "Hello";
    }

    //@GetMapping("/keywords")   just in case
    @GetMapping(value = "/keywords", produces = MediaType.APPLICATION_JSON_VALUE)
    public String keywords(){
        //String kwords = nlpservice.getKeywords();
        return nlpservice.getKeywords();
    }

    //@GetMapping("/texts")
    @GetMapping(value = "/texts", produces = MediaType.APPLICATION_JSON_VALUE)
    public String texts(){
        //String texts = nlpservice.getTexts();
        return nlpservice.getTexts();
    }


}

