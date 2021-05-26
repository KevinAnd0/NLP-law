package com.example.nlpPublicAPI.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class nlpController {

    @GetMapping("/")
    public String index(){
        System.out.println("Test");
        return "Hello";
    }

}

