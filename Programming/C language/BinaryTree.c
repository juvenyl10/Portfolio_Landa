void main()
{
 node *root;
 node *tmp;
 //int i;
 root = NULL;
 /* Inserting nodes into tree */
 insert(&root, 9);
 insert(&root, 4);
 insert(&root, 15);
 insert(&root, 6);
 insert(&root, 12);
 insert(&root, 17);
 insert(&root, 2);
/* Printing nodes of tree */
 printf("Pre Order Display\n");
 print_preorder(root);
 printf("In Order Display\n");
 print_inorder(root);
 printf("Post Order Display\n");
 print_postorder(root);
/* Search node into tree */
 tmp = search(&root, 4);
 if (tmp)
 {
 printf("Searched node=%d\n", tmp->data);
 }
 else
 {
 printf("Data Not found in tree.\n");
 }
 /* Deleting all nodes of tree */
 deltree(root);
}