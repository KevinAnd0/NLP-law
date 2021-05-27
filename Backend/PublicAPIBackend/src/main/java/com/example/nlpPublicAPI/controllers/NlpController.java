package com.example.nlpPublicAPI.controllers;

import com.example.nlpPublicAPI.entities.Keywords;
import com.example.nlpPublicAPI.services.NlpService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
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


}

