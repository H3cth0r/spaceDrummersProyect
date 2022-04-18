using System;
using System.IO;

namespace ReadTextTabs{


        class TabReader{
            public Dictionary<char, int> dictionary_tabs = new Dictionary<char, int>(){
                {'C', 0},
                {'H', 1},
                {'F', 2},
                {'S', 3},
                {'B', 4},
                {'-', 5},
                {'T', 6}
            };

            // Constructor
            public TabReader(string t_txt_file_path){
                txt_file_path = t_txt_file_path;
                read_txt_file();
            }

            // Public attributes and methods
            public string   txt_file_path;
            public string   tabs;

            public List<List<int>> list_tabs = new List<List<int>>();

            public void print_tab_list(){
                foreach(var i in list_tabs){
                    Console.Write("(");
                    foreach(var j in i){
                        Console.Write(j + ",");
                    }
                    Console.Write(")");
                }
            }

            public List<List<int>> get_list_tabs(){
                return list_tabs;
            }
            
            // Private
            private void     read_txt_file(){
                if(File.Exists(txt_file_path)){
                    tabs = File.ReadAllText(txt_file_path);
                }else{
                    Console.WriteLine("File not found");
                    return;
                }

                // splitted txt
                List<string> split_tabs = tabs.Split(',').ToList();
                int split_tabs_length = split_tabs.Count;
                for(int i = 0; i < split_tabs_length; i++){
                    List<int> iterator_list = new List<int>();
                    int length_word = split_tabs[i].Length;
                    for(int j = 0; j < length_word; j++){
                        iterator_list.Add(dictionary_tabs[split_tabs[i][j]]);
                    }
                    iterator_list.Add(i);
                    list_tabs.Add(iterator_list);
                }
            }

        }



    class Program{

        static readonly string txtFile = "txt_tabs/back_in_black.txt";
        static void Main(string[] args){
            TabReader new_reader = new TabReader(txtFile);
            new_reader.print_tab_list();
        }


    }
}